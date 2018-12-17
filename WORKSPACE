git_repository(
		name = "io_bazel_rules_python",
		remote = "https://github.com/bazelbuild/rules_python.git",
		commit = "",
)

load("@io_bazel_rules_python//python:pip.bzl", "pip_repositories")

pip_repositories()

load("@io_bazel_rules_python//python:pip.bzl", "pip_import")

pip_import(
		name = "my_deps",
		requirements = "//path/to:requirements.txt",
)

load("@io_bazel_rules_python//python:pip.bzl", "pip_install")

pip_install()

load(
		"@io_bazel_rules_python//python:python.bzl",
		"py_binary", "py_library", "py_test",
)

py_binary(
		name = "main",
)
