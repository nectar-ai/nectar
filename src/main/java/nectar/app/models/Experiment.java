package nectar.app.models;

import org.springframework.data.annotation.Id;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class Experiment {
    
    @Id
    private String id;
    private GymEnvironment gymEnvironment;
    private int iterations;
    private double[] gamma;
    private double[] lr;
}
