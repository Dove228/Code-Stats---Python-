from dataclasses import dataclass
from typing import Dict, List, Set


@dataclass
class LanguageConfig:
    name: str
    extensions: Set[str]
    single_line_comment: str
    multi_line_comment_start: str
    multi_line_comment_end: str
    nested_comments: bool = False

    def get_comment_patterns(self) -> tuple:
        return (
            self.single_line_comment,
            self.multi_line_comment_start,
            self.multi_line_comment_end,
        )


class LanguageRegistry:
    _languages: Dict[str, LanguageConfig] = {}

    @classmethod
    def register(cls, config: LanguageConfig):
        cls._languages[config.name.lower()] = config
        for ext in config.extensions:
            cls._languages[ext.lower().lstrip(".")] = config

    @classmethod
    def get_language(cls, name_or_ext: str) -> LanguageConfig | None:
        return cls._languages.get(name_or_ext.lower())

    @classmethod
    def get_all_languages(cls) -> List[LanguageConfig]:
        seen = set()
        languages = []
        for item in cls._languages.values():
            if item.name not in seen:
                seen.add(item.name)
                languages.append(item)
        return languages

    @classmethod
    def is_supported(cls, file_path: str) -> bool:
        if "." in file_path:
            ext = file_path.rsplit(".", 1)[-1].lower()
            return ext in cls._languages
        return False


python_config = LanguageConfig(
    name="Python",
    extensions={".py", ".pyw", ".pyi"},
    single_line_comment="#",
    multi_line_comment_start='"""',
    multi_line_comment_end='"""',
    nested_comments=True,
)
LanguageRegistry.register(python_config)

javascript_config = LanguageConfig(
    name="JavaScript",
    extensions={".js", ".mjs", ".cjs", ".jsx"},
    single_line_comment="//",
    multi_line_comment_start="/*",
    multi_line_comment_end="*/",
)
LanguageRegistry.register(javascript_config)

typescript_config = LanguageConfig(
    name="TypeScript",
    extensions={".ts", ".tsx", ".mts", ".cts"},
    single_line_comment="//",
    multi_line_comment_start="/*",
    multi_line_comment_end="*/",
)
LanguageRegistry.register(typescript_config)

java_config = LanguageConfig(
    name="Java",
    extensions={".java"},
    single_line_comment="//",
    multi_line_comment_start="/*",
    multi_line_comment_end="*/",
)
LanguageRegistry.register(java_config)

c_config = LanguageConfig(
    name="C",
    extensions={".c", ".h"},
    single_line_comment="//",
    multi_line_comment_start="/*",
    multi_line_comment_end="*/",
)
LanguageRegistry.register(c_config)

cpp_config = LanguageConfig(
    name="C++",
    extensions={".cpp", ".hpp", ".cc", ".cxx", ".hxx", ".c++", ".h++"},
    single_line_comment="//",
    multi_line_comment_start="/*",
    multi_line_comment_end="*/",
)
LanguageRegistry.register(cpp_config)

csharp_config = LanguageConfig(
    name="C#",
    extensions={".cs"},
    single_line_comment="//",
    multi_line_comment_start="/*",
    multi_line_comment_end="*/",
)
LanguageRegistry.register(csharp_config)

go_config = LanguageConfig(
    name="Go",
    extensions={".go"},
    single_line_comment="//",
    multi_line_comment_start="/*",
    multi_line_comment_end="*/",
)
LanguageRegistry.register(go_config)

rust_config = LanguageConfig(
    name="Rust",
    extensions={".rs"},
    single_line_comment="//",
    multi_line_comment_start="/*",
    multi_line_comment_end="*/",
)
LanguageRegistry.register(rust_config)

ruby_config = LanguageConfig(
    name="Ruby",
    extensions={".rb", ".rake", ".gemspec"},
    single_line_comment="#",
    multi_line_comment_start="=begin",
    multi_line_comment_end="=end",
)
LanguageRegistry.register(ruby_config)

php_config = LanguageConfig(
    name="PHP",
    extensions={".php", ".phtml", ".php3", ".php4", ".php5", ".php7", ".phps"},
    single_line_comment="//",
    multi_line_comment_start="/*",
    multi_line_comment_end="*/",
)
LanguageRegistry.register(php_config)

swift_config = LanguageConfig(
    name="Swift",
    extensions={".swift"},
    single_line_comment="//",
    multi_line_comment_start="/*",
    multi_line_comment_end="*/",
)
LanguageRegistry.register(swift_config)

kotlin_config = LanguageConfig(
    name="Kotlin",
    extensions={".kt", ".kts"},
    single_line_comment="//",
    multi_line_comment_start="/*",
    multi_line_comment_end="*/",
)
LanguageRegistry.register(kotlin_config)

scala_config = LanguageConfig(
    name="Scala",
    extensions={".scala", ".sc"},
    single_line_comment="//",
    multi_line_comment_start="/*",
    multi_line_comment_end="*/",
)
LanguageRegistry.register(scala_config)

html_config = LanguageConfig(
    name="HTML",
    extensions={".html", ".htm", ".xhtml", ".xml"},
    single_line_comment="",
    multi_line_comment_start="<!--",
    multi_line_comment_end="-->",
)
LanguageRegistry.register(html_config)

css_config = LanguageConfig(
    name="CSS",
    extensions={".css", ".scss", ".sass", ".less"},
    single_line_comment="",
    multi_line_comment_start="/*",
    multi_line_comment_end="*/",
)
LanguageRegistry.register(css_config)

sql_config = LanguageConfig(
    name="SQL",
    extensions={".sql", ".ddl", ".dml"},
    single_line_comment="--",
    multi_line_comment_start="/*",
    multi_line_comment_end="*/",
)
LanguageRegistry.register(sql_config)

bash_config = LanguageConfig(
    name="Shell",
    extensions={".sh", ".bash", ".zsh", ".ash", ".dash"},
    single_line_comment="#",
    multi_line_comment_start="",
    multi_line_comment_end="",
)
LanguageRegistry.register(bash_config)

powershell_config = LanguageConfig(
    name="PowerShell",
    extensions={".ps1", ".psm1", ".psd1"},
    single_line_comment="#",
    multi_line_comment_start="<#",
    multi_line_comment_end="#>",
)
LanguageRegistry.register(powershell_config)

yaml_config = LanguageConfig(
    name="YAML",
    extensions={".yml", ".yaml"},
    single_line_comment="#",
    multi_line_comment_start="",
    multi_line_comment_end="",
)
LanguageRegistry.register(yaml_config)

json_config = LanguageConfig(
    name="JSON",
    extensions={".json", ".jsonc"},
    single_line_comment="",
    multi_line_comment_start="",
    multi_line_comment_end="",
)
LanguageRegistry.register(json_config)

toml_config = LanguageConfig(
    name="TOML",
    extensions={".toml"},
    single_line_comment="#",
    multi_line_comment_start="",
    multi_line_comment_end="",
)
LanguageRegistry.register(toml_config)

markdown_config = LanguageConfig(
    name="Markdown",
    extensions={".md", ".mdx", ".markdown"},
    single_line_comment="",
    multi_line_comment_start="<!--",
    multi_line_comment_end="-->",
)
LanguageRegistry.register(markdown_config)

lua_config = LanguageConfig(
    name="Lua",
    extensions={".lua"},
    single_line_comment="--",
    multi_line_comment_start="--[[",
    multi_line_comment_end="]]",
)
LanguageRegistry.register(lua_config)

perl_config = LanguageConfig(
    name="Perl",
    extensions={".pl", ".pm", ".t"},
    single_line_comment="#",
    multi_line_comment_start="=pod",
    multi_line_comment_end="=cut",
)
LanguageRegistry.register(perl_config)

r_config = LanguageConfig(
    name="R",
    extensions={".r", ".R", ".Rmd", ".Rnw"},
    single_line_comment="#",
    multi_line_comment_start="",
    multi_line_comment_end="",
)
LanguageRegistry.register(r_config)

matlab_config = LanguageConfig(
    name="MATLAB",
    extensions={".m"},
    single_line_comment="%",
    multi_line_comment_start="%{",
    multi_line_comment_end="%}",
)
LanguageRegistry.register(matlab_config)

fortran_config = LanguageConfig(
    name="Fortran",
    extensions={".f", ".f90", ".f95", ".f03", ".f08"},
    single_line_comment="!",
    multi_line_comment_start="",
    multi_line_comment_end="",
)
LanguageRegistry.register(fortran_config)

cobol_config = LanguageConfig(
    name="COBOL",
    extensions={".cob", ".cbl", ".cpy"},
    single_line_comment="*",
    multi_line_comment_start="",
    multi_line_comment_end="",
)
LanguageRegistry.register(cobol_config)

pascal_config = LanguageConfig(
    name="Pascal",
    extensions={".pas", ".pp", ".inc"},
    single_line_comment="//",
    multi_line_comment_start="(*",
    multi_line_comment_end="*)",
)
LanguageRegistry.register(pascal_config)

lisp_config = LanguageConfig(
    name="Lisp",
    extensions={".lisp", ".lsp", ".el", ".scm", ".clj"},
    single_line_comment=";",
    multi_line_comment_start="",
    multi_line_comment_end="",
)
LanguageRegistry.register(lisp_config)

haskell_config = LanguageConfig(
    name="Haskell",
    extensions={".hs", ".lhs"},
    single_line_comment="--",
    multi_line_comment_start="{-",
    multi_line_comment_end="-}",
)
LanguageRegistry.register(haskell_config)

erlang_config = LanguageConfig(
    name="Erlang",
    extensions={".erl", ".hrl"},
    single_line_comment="%",
    multi_line_comment_start="",
    multi_line_comment_end="",
)
LanguageRegistry.register(erlang_config)

elixir_config = LanguageConfig(
    name="Elixir",
    extensions={".ex", ".exs"},
    single_line_comment="#",
    multi_line_comment_start="",
    multi_line_comment_end="",
)
LanguageRegistry.register(elixir_config)

clojure_config = LanguageConfig(
    name="Clojure",
    extensions={".clj", ".cljs", ".cljc", ".edn"},
    single_line_comment=";",
    multi_line_comment_start="",
    multi_line_comment_end="",
)
LanguageRegistry.register(clojure_config)

dart_config = LanguageConfig(
    name="Dart",
    extensions={".dart"},
    single_line_comment="//",
    multi_line_comment_start="/*",
    multi_line_comment_end="*/",
)
LanguageRegistry.register(dart_config)

vue_config = LanguageConfig(
    name="Vue",
    extensions={".vue"},
    single_line_comment="//",
    multi_line_comment_start="/*",
    multi_line_comment_end="*/",
)
LanguageRegistry.register(vue_config)

svelte_config = LanguageConfig(
    name="Svelte",
    extensions={".svelte"},
    single_line_comment="//",
    multi_line_comment_start="<!--",
    multi_line_comment_end="-->",
)
LanguageRegistry.register(svelte_config)

makefile_config = LanguageConfig(
    name="Makefile",
    extensions={".mk", "Makefile", "makefile"},
    single_line_comment="#",
    multi_line_comment_start="",
    multi_line_comment_end="",
)
LanguageRegistry.register(makefile_config)

dockerfile_config = LanguageConfig(
    name="Dockerfile",
    extensions={"Dockerfile", "Dockerfile.dev"},
    single_line_comment="#",
    multi_line_comment_start="",
    multi_line_comment_end="",
)
LanguageRegistry.register(dockerfile_config)


def get_language_by_extension(extension: str) -> LanguageConfig | None:
    ext = extension.lower().lstrip(".")
    return LanguageRegistry.get_language(ext)


def get_language_name(extension: str) -> str:
    config = get_language_by_extension(extension)
    return config.name if config else "Unknown"
