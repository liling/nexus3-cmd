all: dist/nexus3-cmd

dist/nexus3-cmd: nexus3-cmd.py
	pyinstaller --onefile \
	            --add-data $(VIRTUAL_ENV)/lib/python3.6/site-packages/nexuscli/api/script/groovy/nexus3-cli-repository-get.groovy:nexuscli/api/script/groovy \
	            --add-data $(VIRTUAL_ENV)/lib/python3.6/site-packages/nexuscli/api/script/groovy/nexus3-cli-repository-create.groovy:nexuscli/api/script/groovy \
	            --add-data $(VIRTUAL_ENV)/lib/python3.6/site-packages/nexuscli/api/script/groovy/nexus3-cli-repository-delete.groovy:nexuscli/api/script/groovy \
	            --add-data $(VIRTUAL_ENV)/lib/python3.6/site-packages/nexuscli/api/script/groovy/nexus3-cli-cleanup-policy.groovy:nexuscli/api/script/groovy \
	            nexus3-cmd.py

.PHONY: clean
clean:
	rm -rf build dist __pycache__
