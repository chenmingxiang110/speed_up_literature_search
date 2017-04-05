package init;
import java.util.*;
import java.io.*;

public class SimpleFileWriter {
	private ArrayList<String> ContentLookUp;
	public void writefile(ArrayList<String> theList, String filename) throws IOException {
		filename = ContentLookUp+filename;
		FileWriter writer = new FileWriter(filename);
		for (String s : theList) {
			writer.append(s);
			writer.append("\n");
			writer.flush();
		}
		writer.close();
	}

}
