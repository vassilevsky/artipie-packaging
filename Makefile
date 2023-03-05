rpm:
	wget https://github.com/artipie/artipie/releases/download/v0.28.0/artipie-v0.28.0-jar-with-dependencies.jar -O artipie.jar
	rpmbuild -bb --build-in-place artipie.spec
