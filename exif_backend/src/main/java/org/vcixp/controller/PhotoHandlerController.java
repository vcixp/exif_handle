package org.vcixp.controller;


import jakarta.annotation.Resource;
import jakarta.servlet.http.HttpServletResponse;
import lombok.extern.slf4j.Slf4j;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;
import org.vcixp.service.PhotoHandlerService;

import java.io.*;

@Slf4j
@RestController
public class PhotoHandlerController {
    @Resource
    private PhotoHandlerService photoHandlerService;

    @PostMapping("/getExifPhoto")
    public String getExifPhoto(@RequestParam("file") MultipartFile multipartFile) throws IOException, InterruptedException {
        return photoHandlerService.getExifPhoto(multipartFile);
    }

    @GetMapping("/download/{filename}")
    public void download(@PathVariable String filename, HttpServletResponse response) {
        photoHandlerService.download(filename, response);
    }
}
