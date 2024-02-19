package com.xbank.bigdata.efthavale.consumer;

import com.mongodb.spark.MongoSpark;
import org.apache.spark.api.java.function.VoidFunction2;
import org.apache.spark.sql.*;
import org.apache.spark.sql.streaming.StreamingQuery;
import org.apache.spark.sql.streaming.StreamingQueryException;
import org.apache.spark.sql.types.DataTypes;
import org.apache.spark.sql.types.StructType;

public class Application {
    public static void main(String[] args) throws StreamingQueryException {

        System.setProperty("hadoop.home.dir","C:\\hadoop-common-2.2.0-bin-master");

        SparkSession sparkSession = SparkSession.builder()
                .master("local").appName("EFT/HAVALE Takip")
                .config("spark.mongodb.output.uri","mongodb://167.172.61.77/finansDB.havaleeft")
                .getOrCreate();

        StructType accountSchema = new StructType()
        .add("iban",DataTypes.StringType)
        .add("oid",DataTypes.IntegerType)
        .add("title",DataTypes.StringType);

        StructType infoSchema = new StructType()
        .add("bank",DataTypes.StringType)
        .add("iban",DataTypes.StringType)
        .add("title",DataTypes.StringType);

        StructType schema=new StructType()
        .add("current_ts", DataTypes.TimestampType)
        .add("balance", DataTypes.IntegerType)
        .add("btype",DataTypes.StringType)
        .add("pid",DataTypes.IntegerType)
        .add("ptype",DataTypes.StringType)
        .add("account",accountSchema)
        .add("info",infoSchema);

        Dataset<Row> loadDS = sparkSession.readStream().format("kafka")
                .option("kafka.bootstrap.servers", "167.172.61.77:9092")
                .option("subscribe", "efthavale").load().selectExpr("CAST(value as STRING)");

        Dataset<Row> rawDS = loadDS.select(functions.from_json(loadDS.col("value"), schema).as("data")).select("data.*");

        Dataset<Row> havaleTypeDS = rawDS.filter(rawDS.col("ptype").equalTo("H"));

        Dataset<Row> volumeDS = havaleTypeDS.groupBy(functions.window(havaleTypeDS.col("current_ts"), "1 minute"),
                havaleTypeDS.col("btype"))
                .sum("balance");

        volumeDS.writeStream().outputMode("complete").foreachBatch(new VoidFunction2<Dataset<Row>, Long>() {
            public void call(Dataset<Row> rowDataset, Long aLong) throws Exception {
                MongoSpark.write(rowDataset).mode("append").save();
            }
        }).start().awaitTermination();


    }
}
