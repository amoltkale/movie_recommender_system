from py4j.java_gateway import java_import

def write_dataframe(spark, sc, df, hdfs_dirname, fname):
    hdfs_p = "hdfs:///" + hdfs_dirname + "/"
    df.coalesce(1).write.csv(hdfs_p, header=True)
    rename_file(spark, sc, hdfs_p, fname)

def rename_file(spark, sc, p, fname):
    java_import(spark._jvm, 'org.apache.hadoop.fs.Path')

    fs = spark._jvm.org.apache.hadoop.fs.FileSystem.get(spark._jsc.hadoopConfiguration())
    file = fs.globStatus(sc._jvm.Path(p + 'part*'))[0].getPath().getName()
    fs.rename(sc._jvm.Path(p + file), sc._jvm.Path(p + fname))