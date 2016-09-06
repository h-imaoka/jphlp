jphlp

# What is ?
Simple helper to build JEMSPath from json output.

# Run

```bash
$ ./jphlp.py < list-commands.json
Commands[].InstanceIds[]
Commands[].RequestedDateTime
Commands[].OutputS3KeyPrefix
Commands[].Parameters.commands[]
Commands[].OutputS3BucketName
Commands[].Status
Commands[].Parameters.executionTimeout[]
Commands[].Parameters.workingDirectory[]
Commands[].ExpiresAfter
Commands[].CommandId
Commands[].DocumentName
Commands[].Comment
```

# Tips
Escape `"` quote when `key` contains `-` or any other char.
https://github.com/jmespath/jmespath.py/issues/98
