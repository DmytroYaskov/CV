LL = tectonic
PP = python3.12
CV_SRCS = ./src
UTILS_DIR = $(CV_SRCS)/utils

generated.tex: $(UTILS_DIR)/content_generator.py $(CV_SRCS)/content.toml
	$(PP) $^ --output=$@

cv: $(CV_SRCS)/main.tex generated.tex
	$(LL) -p --keep-intermediates --keep-logs $< -o .
