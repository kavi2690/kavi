package example;

import java.util.concurrent.TimeUnit;

import org.openqa.selenium.chrome.ChromeDriver;

public class text {
	
	public static void main(String[] args) throws InterruptedException {
		
			System.setProperty("webdriver.chrome.driver", "C:\\Users\\\\Admin\\Downloads\\chromedriver-win64\\chromedriver.exe");
			ChromeDriver c= new ChromeDriver();
			
			c.get("https:www.facebook.com");
			
			c.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
			
			c.manage().window().maximize();
			
			c.findElementByName("email").sendKeys("6380606117");
			
			Thread.sleep(4000);
			
			c.findElementByName("pass").sendKeys("kavi2426");
			
			c.findElementByName("login").click();
			
			c.quit();
		
			
		  // c.findElementByLinkText("Sign up").click();
}}
