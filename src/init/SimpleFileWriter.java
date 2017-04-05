package init;
import java.util.*;
import java.io.*;

public class SimpleFileWriter {
	private String foldername;
	public void writefile(ArrayList<String> theList, String filename) throws IOException {
		foldername = "fileLookUp/";
		filename = foldername+filename;
		FileWriter writer = new FileWriter(filename);
		for (String s : theList) {
			writer.append(s);
			writer.append("\n");
			writer.flush();
		}
		writer.close();
	}

}
