import { fstat, promises as fs } from 'fs';
import { TTLCache } from "./ttlcache";

class SchoolLookup {
    private usernameToBucket: TTLCache<Promise<Map<string, string>>> = null;
    constructor(private csvlocation: string) {
        this.usernameToBucket = new TTLCache(this.readStudentsCsv.bind(this), 1000 * 60 * 60 * 5 /* 5 hours */);
    }

    private async readStudentsCsv(): Promise<Map<string, string>> {
        const studentUsernamesToScoringBucket = new Map<string, string>();

        const contents = (await fs.readFile(this.csvlocation)).toString();
        contents.split('\n').forEach(line => {
            const elements = line.trim().split(',')
            const username = elements[0].trim();
            const bucket = elements[2].trim();

            console.log(`Placing ${username} in ${bucket}`);

            studentUsernamesToScoringBucket.set(username, bucket);
        })

        return studentUsernamesToScoringBucket;
    }

    public async getScoringBucket(username: string): Promise<string> {
        return (await this.usernameToBucket.getValue()).get(username.trim());
    }
}

export default new SchoolLookup("students/students.csv");