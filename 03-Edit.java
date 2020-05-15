import java.lang.reflect.Field;

class Edit
{
	public static void main(String[] args)
	{
		Counter c = new Counter();
		Field[] fields = Counter.class.getDeclaredFields();
		int tickShip;
		try
		{
			fields[1].setAccessible(true);
			fields[1].set(c, 100000000);
			tickShip = (int)fields[1].get(c);
			System.out.println("tickShip = " + tickShip);	
		} catch (Exception e) {
		System.out.println(e);		
}
	}
}
