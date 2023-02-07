import java.util.regex.*;

public class Regex2 {
    public static void main(String[] args) {
        System.out.println(Pattern.matches("[B-J].{2}i.?", "India"));
        System.out.println(Pattern.matches("[amn]", "acd"));
        System.out.println(Pattern.matches("[amn]", "a"));
        System.out.println(Pattern.matches("[^amn]", "c"));
        System.out.println(Pattern.matches("[A-Z]ar[a-z]{5}", "Darshan"));
        System.out.println(Pattern.matches("[xyz]","x"));
        System.out.println(Pattern.matches("[xyz]?","yyyyyzz"));
        System.out.println(Pattern.matches("[MS][a-z]{5}","Monica"));
        System.out.println(Pattern.matches("[xyz]+","yz"));
    }
}
