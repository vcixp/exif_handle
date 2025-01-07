package org.vcixp.service.impl;

import cn.hutool.core.date.DateUtil;
import cn.hutool.core.io.FileUtil;
import jakarta.servlet.http.HttpServletResponse;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.HttpHeaders;
import org.springframework.stereotype.Service;
import org.springframework.web.multipart.MultipartFile;
import org.vcixp.service.PhotoHandlerService;

import java.io.*;
import java.nio.file.Files;
import java.util.UUID;

@Slf4j
@Service
public class PhotoHandlerServiceImpl implements PhotoHandlerService {
    @Value("${app.location}")
    private String location;
    @Value("${app.python-exec}")
    private String pythonExec;
    @Value("${app.python-file}")
    private String pythonFile;

    @Override
    public String getExifPhoto(MultipartFile multipartFile) throws IOException, InterruptedException {
        String folder = getFolder();
        FileUtil.mkdir(folder);
        String ext = FileUtil.extName(multipartFile.getOriginalFilename());
        String srcFile = folder + File.separator + UUID.randomUUID() + "." + ext;
        String fileName = DateUtil.today() + "_" + UUID.randomUUID() + "." + (ext!=null && ext.equalsIgnoreCase("heic") ? "jpg" : ext);
        String toFile = folder + File.separator + fileName;

        String logFile = folder + File.separator + DateUtil.today() + "_" + UUID.randomUUID() + ".log";
        Files.copy(multipartFile.getInputStream(), new File(srcFile).toPath());
        String command = pythonExec + " " + pythonFile + " " + srcFile + " " + toFile + " " + logFile;
        Process exec = Runtime.getRuntime().exec(command);
        exec.waitFor();
        String logs = FileUtil.readUtf8String(logFile);
        if ("ok".equals(logs)) {
            return fileName;
        }
        return null;
    }

    @Override
    public void download(String filename, HttpServletResponse response) {
        String folder = getFolder();
        FileUtil.mkdir(folder);
        String fileStr = folder + File.separator + filename;
        File file = new File(fileStr);
        if (file.exists()) {
            response.addHeader(HttpHeaders.CONTENT_DISPOSITION, "attachment; filename=image.jpg");
            byte[] buffer = new byte[1024];
            FileInputStream fis = null;
            BufferedInputStream bis = null;
            try {
                fis = new FileInputStream(file);
                bis = new BufferedInputStream(fis);
                OutputStream os = response.getOutputStream();
                int i = bis.read(buffer);
                while (i != -1) {
                    os.write(buffer, 0, i);
                    i = bis.read(buffer);
                }
                log.info("下载文件成功，文件：" + fileStr);
            } catch (Exception e) {
                log.error("下载文件失败", e);
            } finally {
                if (bis != null) {
                    try {
                        bis.close();
                    } catch (IOException e) {
                        log.error(e.getMessage(), e);
                    }
                }
                if (fis != null) {
                    try {
                        fis.close();
                    } catch (IOException e) {
                        log.error(e.getMessage(), e);
                    }
                }
            }
        }
    }

    private String getFolder() {
        return location;
    }
}
