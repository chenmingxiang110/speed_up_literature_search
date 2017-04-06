package init;

import java.io.IOException;
import java.util.*;

public class LookUpMain {
	
	public static void main(String[] args) throws IOException {
		String input = "start";
		while(true) {
			System.out.println("Please type the filename!");
			Scanner sc = new Scanner(System.in);
	        if(sc.hasNextLine()) {
	        	String filename = sc.nextLine();
	        	if (filename.equals("quit")) break;
	        	LineContentLookUp lclu = new LineContentLookUp();
	        	SimpleFileWriter sfw = new SimpleFileWriter();
	        	
	        	ArrayList<String> al = lclu.readfile(filename);
	        	sfw.writefile(al, filename);
	        	System.out.println("Successfully write the file!");
	        } else {
	        	System.out.println("Invalid filename!");
	        }
		}
	}

}
