import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Deque;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Queue;
import java.util.Stack;


public class task {
    public static void main(String[] args) {
        Path path = Paths.get("./test.txt");        
        List<List<Character>> data = new ArrayList<>();
        
        try {
            Files.readAllLines(path).forEach((line) -> {
                var charrr = line.toCharArray();
                var chars = new ArrayList<Character>();

                for (char c : charrr) {
                    chars.add(c);
                }
                data.add(chars);
            });;
        } catch (IOException e) {
            System.err.println("ERROR");
        } 

        var plots = new HashMap<Character, List<int[]>>();

        for (int y = 0; y < data.size(); y++){
            for (int x = 0; x < data.getFirst().size(); x++){
                var plant_type = data.get(y).get(x);
                if (plots.containsKey(plant_type)) {
                    List<int[]> plants = plots.get(plant_type);
                    int[] point = {x, y};
                    plants.add(point);
                } else {
                    var plants = new ArrayList<int[]>();
                    int[] point = {x, y};
                    plants.add(point);
                    plots.put(plant_type, plants);
                }
                
            }
        }
        
        var visited = new HashSet<int[]>();

        int[] res = count_plots('R', visited, plots.get('R'));

        for (int i : res) {
            System.out.println(i);
        }
    }

    static boolean contains(Iterable<int[]> iter, int[] point) {
        for(int[] d: iter) {
            if (d[0] == point[0] && d[1] == point[1]) {
                return true;
            }
        }
        return false;
    }

    static int[] count_plots(Character plant_type, HashSet<int[]> visited, List<int[]> plots) {
        visited.add(plots.get(0));
        var count_1 = 0;
        var count_2 = 0;

        for (int[] plant: plots) {
            if (contains(visited, plant)) {
                continue;
            }
            var plot = new Stack<int[]>();
            plot.add(plant);
            var region = new HashSet<int[]>();
            region.add(plant);

            while (plot.size() > 0) {
                int[] current_plant = plot.pop();
                int[][] neighbors = {
                    {current_plant[0] + 1, current_plant[1]}, 
                    {current_plant[0] - 1, current_plant[1]}, 
                    {current_plant[0], current_plant[1] - 1}, 
                    {current_plant[0], current_plant[1] + 1}
                };

                for (int[] neighbor: neighbors) {
                    if (contains(plots, neighbor) && !contains(visited, neighbor)) {
                        visited.add(neighbor);
                        plot.add(neighbor);
                        region.add(neighbor);
                    }
                }
            }
            
            var area = region.size();
            var count_region_1 = 0;
            for (int[] current_plant: region) {
                System.out.println("(" + current_plant[0]+ ", " + current_plant[1] + ")");
                int[][] neighbors = {
                    {current_plant[0] + 1, current_plant[1]}, 
                    {current_plant[0] - 1, current_plant[1]}, 
                    {current_plant[0], current_plant[1] - 1}, 
                    {current_plant[0], current_plant[1] + 1}
                };
                for (int[] neighbor: neighbors) {
                    if (!contains(region, neighbor)) {
                        count_region_1++;
                    }
                }
            }
            System.out.println(count_region_1);
            System.out.println(area);
            count_1 += (count_region_1 * area);

        }
        
        int[] out = {count_1,2};
        return out;
    }
} 