package nectar.app.models;

import org.springframework.data.annotation.Id;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class GymEnvironment {
    
    @Id
    private String id;
    private String environmentName;
    private String environmentPath;
}
