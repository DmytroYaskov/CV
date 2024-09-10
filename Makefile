CC = tectonic
CV_SRCS = ./src
UTILS_DIR = $(CV_SRCS)/utils

cv: $(CV_SRCS)/main.tex
	$(CC) -p $< -o .
