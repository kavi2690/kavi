package example;

import java.util.concurrent.TimeUnit;

import org.openqa.selenium.chrome.ChromeDriver;

public class link {
	public static void main(String[] args) {
		System.setProperty("webdriver.chrome.driver", "C:\\Users\\\\Admin\\Downloads\\chromedriver-win64\\chromedriver.exe");
		ChromeDriver c= new ChromeDriver();
		
		c.get("https://letcode.in/selenium");
		
		c.manage().timeouts().implicitlyWait(2000, TimeUnit.SECONDS);
		
		c.findElementByLinkText("Product").click();

	}
}
