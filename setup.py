from setuptools import setup, find_packages

setup(
    name="vmprof-viewer",
    author="Jonas Haag",
    author_email="jonas@lophus.org",
    version="1.0.0",
    packages=find_packages(),
    description="Standalone browser-based viewer for vmprof",
    url="https://github.com/jonashaag/vmprof-viewer",
    install_requires=[
        "vmprof",
        "django",
    ],
    entry_points = {
        'console_scripts': [
            "vmprofview = vmprof_viewer:main",
    ]},
    classifiers=[
        'License :: OSI Approved :: ISC License (ISCL)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    zip_safe=False,
    include_package_data=True,
)
