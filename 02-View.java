import java.lang.reflect.Field;

class View
{
	public static void main(String[] args)
	{
		Game s = new Game(1, 1);
		Field[] fields = Game.class.getDeclaredFields();
		int time;			


		try
		{
			fields[0].setAccessible(true);
			time = (int)fields[0].get(s);
			System.out.println();
		} catch (Exception e) {
		System.out.println(e);
}
	}
}
