.PHONY: env html clean

env:
	conda env create -f environment.yml

html:
	myst build --html

clean:
	rm -rf _build
    rm -f audio/* figures/*