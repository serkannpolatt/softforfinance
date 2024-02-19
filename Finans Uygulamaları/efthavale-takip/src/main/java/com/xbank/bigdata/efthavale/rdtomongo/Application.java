package com.xbank.bigdata.efthavale.rdtomongo;

import com.mongodb.spark.MongoSpark;
import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.Row;
import org.apache.spark.sql.SparkSession;
import org.apache.spark.sql.types.DataTypes;

public class Application {
    public static void main(String[] args) {
        System.setProperty("hadoop.home.dir","C:\\hadoop-common-2.2.0-bin-master");

        SparkSession sparkSession = SparkSession.builder()
                .master("local").appName("PostgreSQL To MongoDB")
                .config("spark.mongodb.output.uri","mongodb://167.172.61.77/dwh.havaleislem")
                .getOrCreate();

        Dataset<Row> loadDS = sparkSession.read().format("jdbc")
                .option("driver", "org.postgresql.Driver")
                .option("url", "jdbc:postgresql://167.172.61.77/dwh")
                .option("dbtable", "public.havaleislem_csv")
                .option("user", "postgres")
                .option("password", "12345").load();

        Dataset<Row> rowDataset = loadDS.withColumn("balance", loadDS.col("balance").cast(DataTypes.IntegerType));

        MongoSpark.write(rowDataset).mode("append").save();
    }
}
