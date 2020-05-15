import java.lang.reflect.Field;

class Inspect
{
	public static void main(String[] args)
	{
		Field[] fields = Game.class.getDeclaredFields();

		for (Field f : fields)
		{
			System.out.println(f);
		}
	}
}
