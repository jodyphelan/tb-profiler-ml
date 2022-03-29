import setuptools

version = [l.strip() for l in open("tb_profiler_ml/__init__.py") if "version" in l][0].split('"')[1]

setuptools.setup(

	name="tb_profiler_ml",

	version=version,
	packages=["tb_profiler_ml"],
	license="GPLv3",
	long_description="Tool to produce drug resistance predictions based on machine learning models",
	scripts= ["tb-profiler-ml"],
	
)
