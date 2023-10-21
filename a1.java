package example;

import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.interactions.Actions;
import org.testng.annotations.Test;

public class a1 {
	
	 @Test
		public static void main ()throws InterruptedException {
			System.setProperty("webdriver.chrome.driver", "C:\\Users\\\\Admin\\Downloads\\chromedriver-win64\\chromedriver.exe");
			ChromeDriver c= new ChromeDriver();
			
			c.get("https://letcode.in/selenium");
	          WebElement ele = c.findElementByName("Log in");
			
			Actions d1= new Actions(c);
			
//			d1.click(ele).build().perform();
			
//			d1.doubleClick(ele).build().perform();
//			
			d1.contextClick(ele).build().perform();
//			
//			d1.moveToElement(ele).click().build().perform();
//			
//			d1.clickAndHold(ele).build().perform();
//			Thread.sleep(3000);
//			d1.release(ele).build().perform();

}}