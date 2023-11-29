import sys
import pkg_resources
import requests

def get_package_dependencies(package_name, seen_dependencies=None, cache=None):
    if seen_dependencies is None:
        seen_dependencies = set()

    if cache is None:
        cache = {}
    if package_name in seen_dependencies:
        return {}
    if package_name in cache:
        return cache[package_name]

    dependencies = {}

    try:
        # Получаем информацию о пакете
        package = pkg_resources.get_distribution(package_name)

        # Получаем зависимости пакета
        for requirement in package.requires():
            requirement_name = str(requirement)
            if requirement_name != package_name:  # Исключаем самоповторение
                dependencies[requirement_name] = get_package_dependencies(requirement_name, seen_dependencies, cache)

    except (pkg_resources.DistributionNotFound, pkg_resources.VersionConflict):
        pass  # Пропускаем неустановленные пакеты и конфликтующие версии

    if package_name not in seen_dependencies:
        seen_dependencies.add(package_name)

        # Попробуем получить информацию о пакете из кэша или PyPI
        if package_name in cache:
            info = cache[package_name]
        else:
            url = f"https://pypi.org/pypi/{package_name}/json"
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                info = data.get("info", {})
                cache[package_name] = info
            else:
                info = {}

        requires_dist = info.get("requires_dist", [])

        if requires_dist is not None:
            for requirement in requires_dist:
                requirement_name = requirement.split(";")[0].strip()
                if requirement_name != package_name:  # Исключаем самоповторение
                    dependencies[requirement_name] = get_package_dependencies(requirement_name, seen_dependencies, cache)

    return dependencies

def generate_graphviz_text(dependencies, indent=0):
    graph_text = ""
    for package, sub_dependencies in dependencies.items():
        graph_text += "    " * indent + f'"{package}"\n'
        if sub_dependencies:
            graph_text += generate_graphviz_text(sub_dependencies, indent + 1)
    return graph_text

def main():
    package_name = sys.argv[1]
    seen_dependencies = set()
    cache = {}
    dependencies = get_package_dependencies(package_name, seen_dependencies, cache)

    dependencies.pop(package_name, None)

    graphviz_text = f"digraph G {{\n{generate_graphviz_text(dependencies)}}}"
    print(graphviz_text)

if __name__ == "__main__":
    main()