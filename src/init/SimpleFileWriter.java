package init;
import java.util.*;
import java.io.*;

public class SimpleFileWriter {
	private String foldername;
	public void writefile(ArrayList<String> theList, String filename) throws IOException {
		foldername = "fileLookUp/";
		filename = foldername+filename+".csv";
		FileWriter writer = new FileWriter(filename);
		for (String s : theList) {
			String[] theLine = s.split("\t");
			StringBuilder sb = new StringBuilder();
			for (int i = 0 ; i < theLine.length ; i++) {
				sb.append(theLine[i]);
				sb.append(",");
			}
			sb.deleteCharAt(sb.length()-1);
			writer.append(sb.toString());
			writer.append("\n");
			writer.flush();
		}
		writer.close();
	}

}
