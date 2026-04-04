# zeffcodes
Project
public class VirtualizationClass {
    public static void main(String[] args) {
        System.out.println("JVM Name: " + System.getProperty("java.vm.name"));
        System.out.println("OS Name: " + System.getProperty("os.name"));
        System.out.println("Max JVM Memory: "
                + Runtime.getRuntime().maxMemory() / (1024 * 1024) + " MB");
        try {
            int[] arr = new int[500_000_000];
            System.out.println("Memory allocated successfully!");
        } catch (OutOfMemoryError e) {
            System.out.println("OutOfMemoryError occurred!");
        }
    }
}
