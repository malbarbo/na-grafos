.PHONY: default all pdf handout tex clean clean-bin clean-all

SHELL=bash
DEST=target
DEST_PDF=$(DEST)/pdfs
DEST_PDF_HANDOUT=$(DEST)/pdfs/handout
DEST_TEX=$(DEST)/tex
DEST_ZIP=$(DEST)/zips
NA=$(patsubst %/,%,$(dir $(shell find * -wholename '*/notas-de-aula.md')))
NA_PDF=$(addprefix $(DEST_PDF)/, $(addsuffix .pdf, $(NA)))
NA_PDF_HANDOUT=$(addprefix $(DEST_PDF_HANDOUT)/, $(addsuffix .pdf, $(NA)))
NA_TEX=$(addprefix $(DEST_TEX)/, $(addsuffix .tex, $(NA)))
EX=$(patsubst %/,%,$(dir $(shell find * -wholename '*/exercicios.md')))
EX_PDF=$(addprefix $(DEST_PDF)/, $(addsuffix -exercicios.pdf, $(EX)))
EXS=$(patsubst %/,%,$(dir $(shell find * -type d -wholename '*/exemplos')))
EXS_ZIP=$(addprefix $(DEST_ZIP)/, $(addsuffix -exemplos.zip, $(EXS)))
TECTONIC=$(DEST)/bin/tectonic
TECTONIC_VERSION=0.7.1
PANDOC=$(DEST)/bin/pandoc
PANDOC_VERSION=2.14.1
PANDOC_CMD=$(PANDOC) \
		-V mathspec \
		--from markdown-auto_identifiers \
		--pdf-engine=$(CURDIR)/$(TECTONIC) \
		--metadata-file ../metadata.yml \
		--template ../templates/default.latex \
		--to beamer \
		--standalone

default:
	@echo Executando make em paralelo [$(shell nproc) tarefas]
	@make -s -j $(shell nproc) all

all: tex pdf handout ex zip

pdf: $(NA_PDF)

tex: $(NA_TEX)

handout: $(NA_PDF_HANDOUT)

ex: $(EX_PDF)

zip: $(EXS_ZIP)

$(DEST_PDF)/%.pdf: %/notas-de-aula.md $(wildcard %/imagens/) templates/default.latex metadata.yml $(PANDOC) $(TECTONIC)
	@mkdir -p $(DEST_PDF)
	@echo $@
	@cd $$(dirname $<) && \
		../$(PANDOC_CMD) \
		-o ../$@ notas-de-aula.md

$(DEST_PDF_HANDOUT)/%.pdf: %/notas-de-aula.md $(wildcard %/imagens/) templates/default.latex metadata.yml $(PANDOC) $(TECTONIC)
	@mkdir -p $(DEST_PDF_HANDOUT)
	@echo $@
	@cd $$(dirname $<) && \
		../$(PANDOC_CMD) \
		-V classoption:handout \
		-o ../$@ notas-de-aula.md

$(DEST_TEX)/%.tex: %/notas-de-aula.md templates/default.latex metadata.yml $(PANDOC)
	@mkdir -p $(DEST_TEX)
	@echo $@
	@cd $$(dirname $<) && \
		../$(PANDOC_CMD) \
		-o ../$@ notas-de-aula.md

$(DEST_PDF)/%-exercicios.pdf: %/exercicios.md templates/default.latex metadata-ex.yml $(PANDOC) $(TECTONIC)
	@mkdir -p $(DEST_PDF)
	@echo $@
	@cd $$(dirname $<) && \
		../$(PANDOC_CMD) \
			--to latex \
			--metadata-file ../metadata-ex.yml \
			-V papersize=a4 \
			-V geometry='margin=1.5cm' \
			-V fontsize=11pt \
			-o ../$@ exercicios.md

$(DEST_ZIP)/%-exemplos.zip: %/exemplos/*
	@mkdir -p $(DEST_ZIP)
	@zip -o $@ -r $$(dirname $<)
	@touch $@

$(PANDOC):
	mkdir -p $(DEST)
	curl -L https://github.com/jgm/pandoc/releases/download/$(PANDOC_VERSION)/pandoc-$(PANDOC_VERSION)-linux-amd64.tar.gz | tar xz -C $(DEST) --strip-components=1

$(TECTONIC):
	mkdir -p $(DEST)/bin/
	curl -L https://github.com/tectonic-typesetting/tectonic/releases/download/tectonic@$(TECTONIC_VERSION)/tectonic-$(TECTONIC_VERSION)-x86_64-unknown-linux-musl.tar.gz \
		| tar xz -C $(DEST)/bin/

clean:
	@echo Removendo $(DEST_PDF) $(DEST_TEX) $(DEST_ZIP)
	@rm -rf $(DEST_PDF) $(DEST_TEX) $(DEST_ZIP)

clean-bin:
	@echo Removendo $(DEST)/bin
	@rm -rf $(DEST)/bin

clean-all:
	@echo Removendo $(DEST)
	@rm -rf $(DEST)
