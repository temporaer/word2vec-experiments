all:
	echo "Usage: make {download|preproc_cb|preproc_mb}"

download:
	./scripts/get_data.sh

preproc_cb:
	perl preproc.pl data/children_book_dataset/data/cbt_train.txt > data/preproc_childrenbook.txt
	perl preproc.pl data/children_book_dataset/data/cbt_test.txt >> data/preproc_childrenbook.txt
	perl preproc.pl data/children_book_dataset/data/cbt_valid.txt >> data/preproc_childrenbook.txt

preproc_mb:
	perl preproc.pl data/books_large_p1.txt > data/preproc_movie_book.txt
	perl preproc.pl data/books_large_p2.txt >> data/preproc_movie_book.txt


