import java.util.Scanner;
import java.util.regex.Pattern;
import java.util.regex.Matcher;

public class Regex1 {

    public static void main(String[] args) {

        // 1st Way of Regex
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the pattern you want to search.");
        String regexPattern = sc.nextLine();
        sc.close();

        Pattern pattern = Pattern.compile(regexPattern);
        Matcher matcher = pattern.matcher(
                "A Tale of Two Cities, novel by Charles Dickens, published both serially and in book form in 1859. The story is set in the late 18th century against the background of the French Revolution. Although Dickens borrowed from Thomas Carlyle's history, The French Revolution, for his sprawling tale of London and revolutionary Paris, the novel offers more drama than accuracy. The scenes of large-scale mob violence are especially vivid, if superficial in historical understanding.The complex plot involves Sydney Carton's sacrifice of his own life on behalf of his friends Charles Darnay and Lucie Manette. While political events drive the story, Dickens takes a decidedly antipolitical tone, lambasting both aristocratic tyranny and revolutionary excess—the latter memorably caricatured in Madame Defarge, who knits beside the guillotine. The book is perhaps best known for its opening lines, \"It was the best of times, it was the worst of times,\" and for Carton's last speech, in which he says of his replacing Darnay in a prison cell, “It is a far, far better thing that I do, than I have ever done; it is a far, far better rest that I go to, than I have ever known.\" ");

        // compile() ---> It compiles the given regex and returns the instance of a
        // pattern() ---> It compiles the given regex and returns the instance of a pattern
        // matcher() ---> Used to create a matcher that matches the given input with the
        // pattern

        boolean found = false;

        while (matcher.find()) {
            System.out.println("Found the text \" " + matcher.group() + " \" starting at index " + matcher.start()
                    + " and ending at index " + matcher.end() + "\n");
            // group() ---> Used to return the matched sequence
            // start() ---> Returns the starting index
            // end() ---> Returns the ending index
            // matches() ---> Tests whether the given regular expression matches or not
            // groupCount() ---> Returns the total number of the matched sequence
            // find() ---> Used to find the next expression that matches the pattern
            found = true;
        }

        if (found == false) {
            System.out.println("Pattern Not Found in given text. \n");
        }

    }

}
