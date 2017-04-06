package init;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.*;

public class Template_main {

	private static HashMap<String, HashMap<String, Integer>> clickRate;
	private static String foldername;
	
	public static void main(String[] args) {
		
	}
	
	public static void initialization() {
		foldername = "20160205-MicrosoftAcademicGraph/";
		clickRate = new HashMap<String, HashMap<String, Integer>>();
	}
	
	public static void readFile(String filename) {
		BufferedReader br = null;
		FileReader fr = null;
		try {
			fr = new FileReader(filename);
			br = new BufferedReader(fr);
			String sCurrentLine;
			br = new BufferedReader(new FileReader(filename));
			
			int index = 0;
			// skip the firstLine
			sCurrentLine = br.readLine();
			while ((sCurrentLine = br.readLine()) != null) {
				index++;
				if (index % 1000000 == 0) System.out.println(index+" have been read.");
				String[] theLine= sCurrentLine.split(",");
				if (theLine.length < 1) break;
				
				
			}
			
		} catch (IOException e) {
			e.printStackTrace();
		} finally {
			try {
				if (br != null)
					br.close();
				if (fr != null)
					fr.close();
			} catch (IOException ex) {
				ex.printStackTrace();
			}
		}
	}
	
	public static void outputFile() throws IOException {
		FileWriter writer = new FileWriter(makeWriterFileName());
		writer.append("id,sku_id, click_rate");
		writer.append("\n");
		
		writer.close();
	}
	
	public static String makeWriterFileName(){
		long time = System.currentTimeMillis();
		StringBuffer sb = new StringBuffer();
		sb.append("consumption_once_list_");
		sb.append(time);
		sb.append(".csv");
		return sb.toString();
	}


}
