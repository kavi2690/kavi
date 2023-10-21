package example;

import java.io.IOException;

import org.openqa.selenium.chrome.ChromeDriver;

import com.assertthat.selenium_shutterbug.core.Capture;
import com.assertthat.selenium_shutterbug.core.Shutterbug;

public class screen {
	
	public static void main(String[] args) throws IOException {
		System.setProperty("webdriver.chrome.driver", "C:\\Users\\\\Admin\\Downloads\\chromedriver-win64\\chromedriver.exe");
		ChromeDriver c= new ChromeDriver();
		
		c.get("https://letcode.in/selenium");
		
//		File file=c.getScreenshotAs(OutputType.FILE);
//		
//		FileUtils.copyDirectory(file,new File("C:\\Users\\Admin\\Desktop\\selenium\\"+"k.png"));
		
		Shutterbug.shootPage(c, Capture.FULL, true).save("C:\\Users\\Admin\\Desktop\\selenium\\");

	}

}
