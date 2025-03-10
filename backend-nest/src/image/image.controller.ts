import {
    Controller,
    Post,
    UseInterceptors,
    UploadedFile,
    Get,
    Param,
    Res,
    NotFoundException,
  } from '@nestjs/common';
  import { FileInterceptor } from '@nestjs/platform-express';
  import { ImageService } from './image.service';
  import { Response } from 'express';

  @Controller('image')
  export class ImageController {
    constructor(private readonly imageService: ImageService) {}

    @Post('upload')
    @UseInterceptors(FileInterceptor('file'))
    async uploadFile(@UploadedFile() file: Express.Multer.File) {
      return this.imageService.saveImage(file);
    }

    @Get(':id')
    async getImage(@Param('id') id: number, @Res() res: Response) {
      const image = await this.imageService.getImageById(id);
      if (!image) throw new NotFoundException('Image not found');
      res.setHeader('Content-Type', image.mimetype);
      res.send(image.data);
    }
  }
