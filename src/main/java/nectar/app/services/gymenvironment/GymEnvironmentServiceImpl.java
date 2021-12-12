package nectar.app.services.gymenvironment;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.time.Instant;
import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.web.multipart.MultipartFile;

import nectar.app.models.GymEnvironment;
import nectar.app.repositories.GymEnvironmentRepository;

@Service
public class GymEnvironmentServiceImpl implements GymEnvironmentService {

    @Autowired
    private GymEnvironmentRepository environmentRepository;
    
    @Override
    public GymEnvironment saveEnvironmentFile(MultipartFile environmentFile) {
        
        String time = Long.toString(Instant.now().getEpochSecond());
        String originalFileName = environmentFile.getOriginalFilename();
        GymEnvironment environment = new GymEnvironment();

        if(Optional.ofNullable(originalFileName).isPresent()){
            String environmentName = 
                originalFileName.substring(0, originalFileName.indexOf(".py")) + "_" + time;
            String newFileName = environmentName + ".py";
            environment.setEnvironmentName(environmentName);
            try {
                Path path = Paths.get(String.format("src/main/resources/%s", newFileName));
                Files.write(path, environmentFile.getBytes());
                environment.setEnvironmentPath(path.toAbsolutePath().toString());
            } catch (IOException e) {
                e.printStackTrace();
            }
            
        }

        return this.environmentRepository.save(environment);
    }

    @Override
    public GymEnvironment findEnvironmentById(String environmentId) {
        Optional<GymEnvironment> optionalEnvironment = this.environmentRepository.findById(environmentId);
        if (optionalEnvironment.isPresent()) {
            return optionalEnvironment.get();
        }
        else {
            return new GymEnvironment();
        }
    }

    @Override
    public List<GymEnvironment> findAllEnvironments() {
        return this.environmentRepository.findAll();
    }

    @Override
    public void deleteEnvironment(String environmentId) {
        try {
            GymEnvironment environment = this.findEnvironmentById(environmentId);
            Path path = Paths.get(environment.getEnvironmentPath());
            if(Files.exists(path)) {
                Files.delete(path);
            }
            this.environmentRepository.delete(environment);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
