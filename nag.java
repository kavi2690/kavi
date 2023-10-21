package example;

import java.util.concurrent.TimeUnit;

import org.openqa.selenium.chrome.ChromeDriver;

public class nag {
	
	public static void main(String[] args) throws InterruptedException {
		System.setProperty("webdriver.chrome.driver", "C:\\Users\\\\Admin\\Downloads\\chromedriver-win64\\chromedriver.exe");
		ChromeDriver c= new ChromeDriver();
		
		c.get("https://letcode.in/selenium");
		
		c.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
		
		c.manage().window().maximize();
		
	   c.findElementByLinkText("Sign up").click();
	   
	   Thread.sleep(4000);
	   
	  c.navigate().back();
	  
	  Thread.sleep(4000);
	  
	  c.navigate().forward();
	  
	  Thread.sleep(4000);
	  
	  c.navigate().refresh();
	  
	  c.quit();}

}
