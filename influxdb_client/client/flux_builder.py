class qBuilder():
    def __init__(self):
        self.bucket_name = None
        self.start_time = None
        self.stop_time = None
        self.measurement = None
        self.filter_tuples = None
        self.list = None
        self.single = None
        self.build_bucket = ""
        self.build_time = ""
        self.flatten_param = ""
        self.build_filters = ""
        self.build_flatten = ""
        self.build_flux_query = ""


    def bucket(self, bucket):
        self.bucket_name = bucket
        self.build_bucket = f'from(bucket: bucket_name)'
        return self

    def range(self, start, stop):
        self.start_time = start
        self.stop_time = stop
        self.build_time = f'|> range(start: start_time, stop: stop_time)'
        return self

    def build_equals(self, key, value, equality="==", prefix="r",):
        if type(value) == str:
            return f'{prefix}.{key} == "{value}"'
        if type(value) == int:
            return f'{prefix}.{key} {equality} {value}'

    # def filters(self, filters, equality="=="):
    #     self.filter_tuples = filters
    #     filters_queries = []

    #     for filter in filters:
    #         or_query = ' or '.join(
    #             [self.build_equals(filter[0], value, equality) for value in filter[1]])
    #         filters_queries.append(f'|> filter(fn: (r) => {or_query})')
    #         self.build_filters = "".join(filters_queries)
    #     return self

    def filters(self, filters):
        self.filter_tuples = filters
        if isinstance(filters[1], list):
            print(f'type: {type(self.filter_tuples[1])}')
            return self.list_filters(self.filter_tuples)
        if not isinstance(filters[1], list):
            print(f'type: {type(self.filter_tuples[1])}')
            return self.single_filters(self.filter_tuples)


    def list_filters(self, list):
        self.list = list 
        return self 

    def single_filters(self, list):
        self.single = list 
        return self 


    def do(self):
        if self.bucket_name is None:
            raise Exception("Must provide bucket")
        if self.start_time is None:
            raise Exception("Must provide start time")
        if self.stop_time is None:
            raise Exception("Must provide stop time")

        self.build_flux_query = f'bucket_name = "{self.bucket_name}"\n' + f'start_time = "{self.start_time}"\n' + f'stop_time = "{self.stop_time}"\n' + f'filters = "{self.filter_tuples}"\n' + str(self.build_bucket) + str(self.build_time) + str(self.build_filters) + str(self.build_flatten)
        return self

# q = qBuilder().bucket("test").range("-1hr","now()").filters(filters=[("_measurement", "abc")).do()
# print(str(q.build_flux_query))

q = qBuilder().filters(filters=("_measurement", ["1", "2"]))
print(str(q.list))

q1= qBuilder().filters(filters=("_measurement", "1"))
print(str(q1.single))