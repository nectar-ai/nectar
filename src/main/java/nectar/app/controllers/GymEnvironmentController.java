package nectar.app.controllers;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.multipart.MultipartFile;

import nectar.app.models.GymEnvironment;
import nectar.app.services.gymenvironment.GymEnvironmentService;

@RestController
@RequestMapping("/api/v1/gym-environments")
public class GymEnvironmentController {
    
    @Autowired
    private GymEnvironmentService environmentService;

    @GetMapping(value = {"/"})
    public List<GymEnvironment> findAllEnvironments(){
        return this.environmentService.findAllEnvironments();
    }

    @GetMapping(value = {"/{environmentId}"})
    public GymEnvironment findEnvironmentById(@PathVariable String environmentId) {
        return this.environmentService.findEnvironmentById(environmentId);
    }

    @PostMapping(value = {"/"})
    public GymEnvironment saveEnvironment(@RequestParam("file") MultipartFile environment) {
        return this.environmentService.saveEnvironmentFile(environment);
    }

    @DeleteMapping(value = {"/{environmentId}"})
    public ResponseEntity<String> deleteEnvironment(@PathVariable String environmentId) {
        try {
            this.environmentService.deleteEnvironment(environmentId);
            return new ResponseEntity<>(HttpStatus.OK);
        } catch (Exception e){
            return new ResponseEntity<>(HttpStatus.OK);
        }
    }
}
