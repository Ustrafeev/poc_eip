import { Injectable } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { Repository } from 'typeorm';
import { Image } from './image.entity';

@Injectable()
export class ImageService {
  constructor(
    @InjectRepository(Image)
    private imageRepo: Repository<Image>,
  ) {}

  async saveImage(file: Express.Multer.File): Promise<Image> {
    const image = this.imageRepo.create({
      filename: file.originalname,
      data: file.buffer,
      mimetype: file.mimetype,
    });
    return this.imageRepo.save(image);
  }

  async getImageById(id: number): Promise<Image | null> {
    return this.imageRepo.findOneBy({ id });
  }
}
