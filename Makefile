all: dist/nexus3-cmd

dist/nexus3-cmd: nexus3-cmd.py
	pyinstaller --onefile nexus3-cmd.py

.PHONY: clean
clean:
	rm -rf build dist __pycache__
