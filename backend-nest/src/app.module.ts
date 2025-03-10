import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';
import { ImageModule } from './image/image.module';

@Module({
  imports: [
    TypeOrmModule.forRoot({
      type: 'postgres', // or 'mysql'
      host: 'localhost',
      port: 5432,        // or 3306 for MySQL
      username: 'mike',
      password: 'mike',
      database: 'dbnest',
      entities: [__dirname + '/**/*.entity{.ts,.js}'],
      synchronize: true, // don't use in production
    }),
    ImageModule,
  ],
})
export class AppModule {}
