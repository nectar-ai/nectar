package nectar.app.services.gymenvironment;

import java.util.List;

import org.springframework.web.multipart.MultipartFile;

import nectar.app.models.GymEnvironment;

public interface GymEnvironmentService {
    
    public GymEnvironment saveEnvironmentFile(MultipartFile environment);
    public GymEnvironment findEnvironmentById(String environmentId);
    public List<GymEnvironment> findAllEnvironments();
    public void deleteEnvironment(String environmentId);
}
