import { Entity, PrimaryGeneratedColumn, Column } from 'typeorm';

@Entity()
export class Image {
  @PrimaryGeneratedColumn()
  id: number;

  @Column()
  filename: string;

  @Column({ type: 'bytea' }) // <-- Use 'longblob' for MySQL
  data: Buffer;

  @Column()
  mimetype: string;
}
