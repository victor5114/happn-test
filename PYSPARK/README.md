# Pre requisites

Install Docker + Docker Compose on your machine

# Comments
I'm not used working with PySpark so I tried different approach for the sake of this exercise.
The first approach is basically wrapping SQL query and the other is using PySpark syntax.
Both came out with similar results and complexity.

# Run script

From the `PYSPARK` folder

Simply run `docker run --rm -it -p 4040:4040 -v $(pwd)/main.py:/main.py -v $(pwd)/data:/tmp/data gettyimages/spark bin/spark-submit /main.py`
This command will create two outputs folders inside `data/`

# Develop and tests

1. `docker-compose up`
2. `docker exec -it docker-spark_master_1 /bin/bash`
3. `bin/pyspark`

# Resources
[Run Spark in Docker](https://github.com/gettyimages/docker-spark)