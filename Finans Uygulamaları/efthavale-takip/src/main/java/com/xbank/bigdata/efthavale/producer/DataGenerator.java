package com.xbank.bigdata.efthavale.producer;

import org.json.simple.JSONObject;

import java.io.File;
import java.io.FileNotFoundException;
import java.sql.Timestamp;
import java.util.*;

public class DataGenerator {

    public static List<String> names=new ArrayList<>();
    public static List<String> surnames=new ArrayList<>();
    public static Random r=new Random();
    public static int pid=10000;
    public DataGenerator() throws FileNotFoundException {
        File fileName=new File("C:\\isimler.txt");
        File fileSurname=new File("C:\\soyisimler.txt");
        Scanner fileNameScanner=new Scanner(fileName);
        Scanner fileNameSurname=new Scanner(fileSurname);
        while (fileNameScanner.hasNext()){
            names.add(fileNameScanner.nextLine());
        }

        while (fileNameSurname.hasNext()){
            surnames.add(fileNameSurname.nextLine());
        }
    }

    public String generate(){

        Timestamp timestamp=new Timestamp(System.currentTimeMillis());

        //List<String> btype = Arrays.asList("TL", "USD", "EUR");
        List<Integer> islemno = Arrays.asList(1000, 1001, 2000, 2001);

        JSONObject data = new JSONObject();

            data.put("pid",pid++);
            data.put("ptype",islemno.get(r.nextInt(islemno.size())));

            JSONObject account = new JSONObject();
        data.put("oid",generateID());
        data.put("title",nameSurnameGenerator());
            //account.put("iban","TR"+generateID());

            //data.put("account",account);

            //JSONObject info = new JSONObject();
            //info.put("title",nameSurnameGenerator());
            //info.put("iban","TR"+generateID());
            //info.put("bank","X Bank");

           // data.put("info",info);

            data.put("balance",r.nextInt(9999-0)+0);
            //data.put("btype",btype.get(r.nextInt(btype.size())));


        long offset = Timestamp.valueOf("2020-08-03 02:00:00").getTime();
        long end = Timestamp.valueOf("2020-08-03 23:59:00").getTime();
        long diff = end - offset + 1;
        Timestamp rand = new Timestamp(offset + (long) (Math.random() * diff));
            data.put("current_ts",rand.toString());

        return data.toJSONString();
    }

    public static int generateID(){
        int numbers = r.nextInt(999-50)+0;
        return numbers;
    }

    public static String nameSurnameGenerator(){
        String name = names.get(r.nextInt(names.size()));
        String surname = surnames.get(r.nextInt(surnames.size()));

        return name+" "+surname;
    }
}
