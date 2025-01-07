package org.vcixp.service;

import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.multipart.MultipartFile;

import java.io.IOException;

public interface PhotoHandlerService {
    String getExifPhoto(MultipartFile multipartFile) throws IOException, InterruptedException;

    void download(String filename, HttpServletResponse response);
}
