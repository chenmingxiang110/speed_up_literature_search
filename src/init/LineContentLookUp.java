package init;
import java.io.*;
import java.util.ArrayList;

public class LineContentLookUp {
	
	private String foldername;
	private ArrayList<String> ContentLookUp;
	
	public ArrayList<String> readfile(String filename) {
		initialization();
		filename = foldername+filename;
		readFile(filename);
		return ContentLookUp;
	}
	
	private void initialization() {
		foldername = "20160205-MicrosoftAcademicGraph/";
		ContentLookUp = new ArrayList<String>();
	}
	
	private void readFile(String filename) {
		BufferedReader br = null;
		FileReader fr = null;
		try {
			fr = new FileReader(filename);
			br = new BufferedReader(fr);
			String sCurrentLine;
			br = new BufferedReader(new FileReader(filename));
			
			int index = 0;
			while ((sCurrentLine = br.readLine()) != null) {
				index++;
				if (index >= 100) break;
				ContentLookUp.add(sCurrentLine);
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
	
	public void printLookUp() {
		if (ContentLookUp.size() == 0) {
			System.out.println("There is no content been read.");
			return;
		}
		for (String s : ContentLookUp) {
			System.out.println(s);
		}
	}

}
