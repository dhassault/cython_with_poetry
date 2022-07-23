from Cython.Build import cythonize

exclude_list = [
    "sample_package/excluded_module/**",
]
compiler_directives = {"language_level": 3, "embedsignature": True}


def build(setup_kwargs):
    setup_kwargs.update(
        {
            "name": "sample-package",
            "package": ["sample-package"],
            # https://cython.readthedocs.io/en/latest/src/userguide/source_files_and_compilation.html#cythonize-arguments
            "ext_modules": cythonize(
                module_list="sample_package/**/*.py",
                exclude=exclude_list,
                compiler_directives=compiler_directives,
                nthreads=5,
            ),
        }
    )
