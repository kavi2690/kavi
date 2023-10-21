package example;

import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

public class get {
	
	public static void main(String[] args) {
		System.setProperty("webdriver.chrome.driver", "C:\\Users\\Admin\\Downloads\\chromedriver-win64\\chromedriver.exe");
		ChromeDriver n= new ChromeDriver();
		
		n.get("https://letcode.in/selenium");
		
		WebElement e = n.findElementByXPath("//*[@id=\"navbar-menu\"]/div[1]/a[2]");
		
		System.out.println( e.getText());
		
		n.quit();

	}

}
